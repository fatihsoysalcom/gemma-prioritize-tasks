import heapq

def prioritize_tasks(tasks, num_top_tasks=3):
    """Prioritizes tasks based on urgency and importance.

    Args:
        tasks (list): A list of dictionaries, where each dictionary
                      represents a task and has 'name', 'urgency', and 'importance' keys.
        num_top_tasks (int): The number of top priority tasks to return.

    Returns:
        list: A list of the top priority tasks.
    """
    # Calculate a priority score. Higher score means higher priority.
    # We can use a simple formula like urgency * importance.
    # For heapq (min-heap), we'll store negative scores to simulate a max-heap.
    scored_tasks = []
    for task in tasks:
        score = task['urgency'] * task['importance']
        # Store as (-score, task_name) for max-heap behavior
        scored_tasks.append((-score, task['name']))

    # Use heapq to efficiently find the top N tasks
    # heapq.nsmallest will return the N smallest elements, which correspond to
    # the N largest scores due to the negative sign.
    top_tasks_with_scores = heapq.nsmallest(num_top_tasks, scored_tasks)

    # Extract just the task names from the results
    top_task_names = [task_name for score, task_name in top_tasks_with_scores]

    return top_task_names

if __name__ == "__main__":
    # Example tasks with urgency (1-5) and importance (1-5)
    all_tasks = [
        {'name': 'Raporu Tamamla', 'urgency': 4, 'importance': 5},
        {'name': 'E-postaları Kontrol Et', 'urgency': 3, 'importance': 2},
        {'name': 'Yeni Özellik Geliştir', 'urgency': 5, 'importance': 4},
        {'name': 'Toplantı Notlarını Düzenle', 'urgency': 2, 'importance': 3},
        {'name': 'Müşteri Çağrısı Yap', 'urgency': 4, 'importance': 4},
        {'name': 'Kod İncelemesi', 'urgency': 3, 'importance': 5},
        {'name': 'Öğle Yemeği Molası', 'urgency': 1, 'importance': 1}
    ]

    print("Tüm Görevler:")
    for task in all_tasks:
        print(f"- {task['name']} (Aciliyet: {task['urgency']}, Önem: {task['importance']})")
    print("\n---")

    # Let Gemma pick the top 3 tasks
    gemma_top_tasks = prioritize_tasks(all_tasks, num_top_tasks=3)

    print("Gemma'nın Seçtiği En Önemli 3 Görev:")
    for task_name in gemma_top_tasks:
        print(f"- {task_name}")

    print("\nGeri kalan görevler bekleyebilir.")
